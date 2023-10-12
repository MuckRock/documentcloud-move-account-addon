"""
This DocumentCloud Add-On allows you to bulk edit documents
"""

from documentcloud.addon import AddOn
from documentcloud.exceptions import APIError
from documentcloud.toolbox import grouper

BULK_LIMIT = 25


class MoveAccount(AddOn):
    """Change the owning account for all documents"""

    def main(self):
        if not self.documents:
            self.set_message("Please select at least one document.")
            return
            
        me = self.client.users.get("me")
        users_orgs = me.organizations
        if self.data["user"] != me.username:
            self.set_message(
                f"Error: Username did not match.  Expecting: {me.username}, "
                f"you typed: {self.data['user']}"
            )
            raise ValueError
        new_org_id = self.data.get("new_org_id")
        if new_org_id and new_org_id not in users_orgs:
            self.set_message(
                "Error: If new organization ID is set, "
                "it must be an organization you belong to"
            )
            raise ValueError

        try:
            new_user = self.client.users.get(self.data["new_user_id"])
        except APIError as exc:
            self.set_message(f"Error: {exc.error}")
            raise
        if not (set(users_orgs) | set(new_user.organizations)):
            self.set_message(
                "Error: You may only transfer your documents to a user in the "
                "same organization as yourself"
            )
            raise ValueError

        # fetch 25 documents at a time, and bulk edit them in one call
        documents = self.client.documents.search(self.query, per_page=BULK_LIMIT)
        count = 0
        data = {"user": self.data["new_user_id"]}
        if new_org_id:
            data["organization"] = new_org_id
        for page_documents in grouper(documents, BULK_LIMIT):
            json = [
                {"id": d.id, **data}
                for d in page_documents
                if d is not None
                # you must own the document
                and d.user_id == me.id
                # and it must either not be public or in an organization with you
                and (d.access != "public" or d.organization_id in users_orgs)
            ]
            count += len(json)
            try:
                self.client.patch("documents/", json=json)
            except APIError as exc:
                self.set_message(f"Error: {exc.error}")
                raise

        self.set_message(f"Succesfully transferred {count} documents")


if __name__ == "__main__":
    MoveAccount().main()
