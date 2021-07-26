<template> 
  <div class="margin-bottom">  
      <h3>Dependency Parse Table:</h3>    
      <div align = "center">
      <table class="table table-striped table-bordered table-hover">
          <thead class="thead-dark">
          <tr>
              <th>ID</th>
              <th>Form</th>
              <th>POS</th>
              <th>Head</th>
              <th>Dependency Label</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for = "info in parsed_info" :key = "info.index">
              <td>{{ info.index }} </td>
              <td>{{ info.form }} </td>
              <td>{{ info.pos }} </td>
              <td>{{ info.head }} </td>
              <td>{{ info.label }} </td>
          </tr>
          </tbody>
      </table>
      </div>
  </div>
</template>

<script>
export default {
  name: 'ParseTable',
  props: ['parsed_info']
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
</style>