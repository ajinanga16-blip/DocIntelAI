import requests

from bs4 import BeautifulSoup
from pypdf import PdfReader


class StyleExtractor:

    def extract_from_pdf(
        self,
        file_path
    ):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages[:30]:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text

    def extract_from_docx(
        self,
        file_path
    ):
        pass

    def extract_from_url(
        self,
        url
    ):

        response = requests.get(url)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        return soup.get_text(
            separator="\n",
            strip=True
        )