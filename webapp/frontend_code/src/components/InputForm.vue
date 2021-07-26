<template>
  <div class="container margin-bottom">
    <div class="loader" v-if="isloading"></div>
    <form @submit="formSubmit">
      <fieldset :disabled="isloading">
        <div class="row">
          <div class="col-sm">
            <div class="form-group">
              <textarea class="form-control" v-model="form.sentence" id="sentenceinput" 
                placeholder="Enter a Vietnamese sentence to parse" aria-describedby="Enter a Vietnamese sentence to parse" 
                rows="6"/>        
            </div>
          </div>

          <div class="col-sm">
            <div class="form-group">
              <p >Model to use:</p>
              <div class="row">
                <div class="col-sm-12">
                  <input type="radio" class="form-check-input" id="parsemodel_vncorenlp" name="parsemodel" value="vncorenlp" v-model="form.parsemodel" checked/>
                  <label class="form-check-label" for="parsemodel_vncorenlp">VNCoreNLP (Lightweight)</label>
                </div>
                <div class="col-sm-12">
                  <input type="radio" class="form-check-input" id="parsemodel_phonlp" name="parsemodel" value="phonlp" v-model="form.parsemodel" />
                  <label class="form-check-label" for="parsemodel_phonlp">PhoNLP (SOTA)</label>
                </div>
                <div class="col-sm-12">
                  <input type="radio" class="form-check-input" id="parsemodel_jptdp" name="parsemodel" value="jptdp" v-model="form.parsemodel" />
                  <label class="form-check-label" for="parsemodel_jptdp">jPTDP (Lightweight)</label>
                </div>
              </div>
            </div>            
          </div>
        </div>      
        <div class="form-group button-group">          
          <button class="btn btn-primary">Parse</button>
        </div>
      </fieldset>
    </form>    
    <div v-if="error">
      <strong>{{error}}</strong>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InputForm',
  data: function() {
    return {
          form: {
              sentence: "",
              parsemodel: "vncorenlp"
          },
          isloading: false,
          error: ""
      }
  },
  methods: {
      formSubmit(e) {
          e.preventDefault();
          this.isloading = true;
          let currentObject = this;
          const options = { 
            method: 'POST', 
            url: "/api/dependency_parse", 
            data: { 
              sentence: currentObject.form.sentence,
              parsemodel: currentObject.form.parsemodel
            }, 
            headers: { 'xsrfCookieName': 'csrftoken', 'xsrfHeaderName': 'X-CSRFToken'}, 
            withCredentials: true } 
          this.axios(options).then(function (response) {
              currentObject.error = "";
              currentObject.$emit('parsed', response.data);
          })
          .catch(function (error) {              
              currentObject.error = error;
              currentObject.$emit('parsed', "");
          })
          .finally(() => {
              currentObject.isloading = false;
          });
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
.margin-bottom {
  margin-bottom: 15px;
}
div.container {
  text-align: left;
  margin-top: 2em;
}
div.form-group {
  margin-top: 1em;
}
p {
  margin-bottom: 0.5em;
}
.loader{  /* Loader Div Class */
  position: absolute;
  top:0px;
  right:0px;
  width:100%;
  height:100%;
  background-color:#eceaea;
  background-image: url('../assets/ajax-loader.gif');
  background-size: 50px;
  background-repeat:no-repeat;
  background-position:center;
  z-index:10000000;
  opacity: 0.4;
  filter: alpha(opacity=40);
}
.form-check-input {
  margin-right: 0.5em;
}
</style>
