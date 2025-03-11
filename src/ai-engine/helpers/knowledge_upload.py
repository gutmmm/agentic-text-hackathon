from agno.knowledge.pdf import PDFKnowledgeBase
from agno.knowledge.csv import CSVKnowledgeBase
from agno.vectordb.qdrant import Qdrant

from dotenv import load_dotenv

load_dotenv()


class Knowledge:
    def __init__(self, collection_name):
        self.vector_db = Qdrant(
            collection=collection_name,
            url="https://5eb77237-553d-4645-ab98-ac78733609ca.eu-central-1-0.aws.cloud.qdrant.io",
            api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.aJ0SiCOIcLEzMZcoeeDhYIvt4L1mGkKO8g8O9EanuUU",
        )

    def upload_pdf(self, path):
        knowledge_base = PDFKnowledgeBase(
            path=path,
            vector_db=self.vector_db,
        )
        knowledge_base.load(recreate=True, upsert=True)

    def upload_csv(self, path):
        orders_csv = CSVKnowledgeBase(
            path=path,
            vector_db=self.vector_db,
        )
        orders_csv.load(recreate=True, upsert=True)


if __name__ == "__main__":
    knowledge = Knowledge("")
    knowledge.upload_pdf(path="About_Us.pdf")
    # knowledge.upload_csv(path=path)
