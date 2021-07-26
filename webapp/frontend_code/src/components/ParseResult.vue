<template>
  <div class="container" v-if="parsed_result">  
    <div class="margin-bottom">  
      <h3>Dependency Parse Result:</h3>
      <div class='row'>
        <div class="col-sm-4">
          <button class="btn btn-primary" :disabled="disable_previous" v-on:click="show -= 1">Previous</button>
        </div>
        <div class="col-sm-4">
          <h4>Sentence {{ show+1 }} of {{ num_of_sentences }}</h4>  
        </div>
        <div class="col-sm-4">
          <button class="btn btn-primary" :disabled="disable_next" v-on:click="show += 1">Next</button>
        </div>
      </div>
      <ParseTable v-bind:parsed_info="parsed_result"/>
      <ParseTree v-bind:parsed_info="parsed_result"/>
    </div>
  </div>
</template>

<script>
import ParseTable from './ParseTable.vue'
import ParseTree from './ParseTree.vue'

export default {
  name: 'ParseResult',
  components: {
    ParseTable,
    ParseTree
  },
  props: ['parsed_sentences'],
  data: function() {
    return {
      show: 0,
      disable_previous: true,
    }
  },
  computed: {
      parsed_result: function() {
          let sentence_to_show = this.parsed_sentences[this.show];
          return sentence_to_show;
      },
      num_of_sentences: function() {
          return this.parsed_sentences.length;
      },
      disable_next: function() {
          return this.show == (this.num_of_sentences - 1)
      }
  },
  watch: {
      parsed_sentences: function() {
        this.show = 0;
      },
      show: function() {
        this.disable_previous = (this.show == 0);
        this.disable_next = (this.show == (this.num_of_sentences - 1));
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0;
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
.btn-primary {
  width: 6em;
}
</style>