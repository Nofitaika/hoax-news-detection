import streamlit as st
from streamlit.logger import get_logger
import tensorflow as tf
import ktrain 
from ktrain import text

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="CekDulu!",
        page_icon="🧐",
    )

    st.write("# :blue[CekDulu!] 🧐")

    st.sidebar.success("Cek informasi benar atau hoax")

    st.markdown(
        """
        CekDulu adalah website yang dapat kamu manfaatkan untuk memprediksi kemungkinan suatu informasi dapat dipercaya kebenarannya atau tidak.
        
    """
    )

            
    st.write("### Dapat informasi? Cek dulu kebenarannya!")
    txt = st.text_area(
    "Tuliskan di sini 👇",
    "",
    )
    @st.cache_resource
    def import_and_predict(text_data):
            model= ktrain.load_predictor('fakenews_predictor_indobert')
            prediction = model.predict(text_data)
            prediction_proba = model.predict(text_data, return_proba=True)

            if prediction == 'truth':
                prediction_class = 'BENAR'
            else:
                prediction_class = 'HOAX'
            return prediction_class, prediction_proba
    
    def import_and_predict_hoax_class(text_data):
            model= ktrain.load_predictor('classification_hoax_nbsvm')
            prediction = model.predict(text_data)
            prediction_proba = model.predict(text_data, return_proba=True)

            return prediction, prediction_proba

    if st.button('Cek', type="primary"):
        if len(txt) > 0:
            pred_class, pred_proba = import_and_predict(txt)
            prediction, prediction_proba = import_and_predict_hoax_class(txt) 
            st.success("#### Informasi ini diduga " + pred_class + ' dengan probability ' + str(round(max(pred_proba) * 100, 2)) + '%')
            if pred_class == 'HOAX':
                st.success(str(round(max(prediction_proba) * 100, 2)) + '%' + ' kemungkinan ' + prediction)

        else:
            st.error('Oooppss! Kamu belum menuliskan informasinya.')

    # st.set_option('deprecation.showfileUploaderEncoding', False)
    # @st.cache_resource
    # def load_model():
    #     model= ktrain.load_predictor('fakenews_predictor_indobert')
    #     return model

    # # with st.spinner('Model is being loaded..'):
    # model=load_model()

if __name__ == "__main__":
    run()