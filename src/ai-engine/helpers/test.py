import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.csv_toolkit import CsvTools


url = "https://agno-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"
response = requests.get(url)

imdb_csv = Path(__file__).parent.joinpath("imdb.csv")
imdb_csv.parent.mkdir(parents=True, exist_ok=True)
imdb_csv.write_bytes(response.content)
