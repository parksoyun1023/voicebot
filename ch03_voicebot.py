import streamlit as st

#####메인 함수#####
def main():
    #기본설정
    st.set_page_config(
        page_title="채팅비서 프로그램",
        layout="wide")
    
    #제목
    st.header("채팅비서 프로그램")

    #구분선
    st.markdown("---")

    #기본설명
    with st.expander("채팅비서 프로그램에 관하여",expanded=True):
        st.write(
        """
        -채팅비서 프로그램은 수업시간에 배운 음성비서 프로그램을 변형시킨 문제 입니다
        -음성기능을 빼고 채팅 기능만 가능하게끔 수정하였습니다.
        
        """
        )

    #사이드바 생성
    with st.sidebar:

        #Open AI API키 입력받기
        st.session_state["OPENAI_API"] = st.text_input(label="OPENAI API 키",placeholder="Enter Your API Key", value="",type="password")

        st.markdown("---")

        #GPT 모델을 선택하기 위한 라디오 버튼을 생성
        model = st.radio(label="GPT 모델", options=["gpt-4","gpt-3.5-turbo"])

        st.markdown("")

        #리셋버튼
        

if __name__=="__main__":
    main()