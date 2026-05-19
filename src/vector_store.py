from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv  #importaing the .env file from .env
load_dotenv()

class VectorStoreBuilder:   # Initializing the function by passing the path and model name
    def __init__(self,csv_path:str,persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    
    def build_and_save_vectorstore(self):  #building the vector database
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )

        data = loader.load() #Loading the csv file

        splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0) #splitting the text inside the csv files using splitter
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(texts,self.embedding,persist_directory=self.persist_dir) #saving the splitted texts in embedded form in chroma DB
        db.persist()

    def load_vector_store(self): #If the vector is created and don't want to create again and again then we can use these to load the vector database
        return Chroma(persist_directory=self.persist_dir,embedding_function=self.embedding)


