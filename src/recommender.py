from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0)  #Temperature=0 , these no more extra creation from LLM on it's own
        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(  #Using RetrievalQA we are initiating the question and answer chain
            llm = self.llm,
            chain_type = "stuff",
            retriever = retriever,
            return_source_documents = True,
            chain_type_kwargs = {"prompt":self.prompt}
        )

    def get_recommendation(self,query:str):
        result = self.qa_chain({"query":query})  #These will br providing the resultin in json format with lot of bunch of data
        return result['result']   #In the result we are fetching the result value