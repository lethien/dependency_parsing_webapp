<template>
  <section>
    <div class="hello">
      <div>
        <h1>Dependency Parsing for Vietnamese Language</h1>
        <h3>NLP 2021 - JVN Institute </h3>
        <img alt="Vue logo" src="../assets/logo.png"/>
      </div>
      <p>
        This is a webapp project to demonstrate three Dependency Parsing models:
        <ul>
          <li>VNCoreNLP (<a href="https://github.com/vncorenlp/VnCoreNLP" target="_blank" rel="noopener">https://github.com/vncorenlp/VnCoreNLP</a>)</li>
          <li>PhoNLP (<a href="https://github.com/VinAIResearch/PhoNLP" target="_blank" rel="noopener">https://github.com/VinAIResearch/PhoNLP</a>)</li>
          <li>jPTDP (<a href="https://github.com/datquocnguyen/jPTDP" target="_blank" rel="noopener">https://github.com/datquocnguyen/jPTDP</a>)</li>
        </ul>
      </p>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HelloMessage'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 10px 0 0;
}
ul {
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
img {
  height: 5em;
}
</style>
