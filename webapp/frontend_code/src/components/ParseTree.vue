<template>
  <div class="container" v-if="parsed_info">  
    <div class="margin-bottom" :key="parseTreeNum"> 
        <div>
            <h3>Dependency Parse Tree:</h3> 
            <p>You can drag the graph to view</p>
        </div>
        <div class="graph-container">
            <vue-tree
            style="width: 100%; height: 1000px; border: 1px solid gray;"
            :dataset="treeData"
            :config="treeConfig"
            >
                <template v-slot:node="{ node, collapsed }">
                    <div class="rich-media-node" :style="{ border: collapsed ? '2px solid grey' : '' }">            
                        <span style="padding: 4px 0; font-weight: bold;">{{ node.label }}</span>
                        <span style="padding: 4px 0; font-weight: bold; font-size: 2em;">{{ node.form }}</span>
                        <span style="padding: 4px 0; font-weight: bold;">{{ node.pos }}</span>
                    </div>
                </template>
            </vue-tree>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ParseTree',
  props: ['parsed_info'],
  data: function() {
    return {
        parseTreeNum: 0,
        treeConfig: { nodeWidth: 200, nodeHeight: 80, levelHeight: 200 }
    }
  },
  computed: {
      treeData: function() {
          let parse_tree = build_dependency_node(this.parsed_info, "0");
          return parse_tree;
      }
  },
  watch: {
      treeData: function() {
        this.parseTreeNum += 1;
      }
  }
}

function build_dependency_node(infos, node_id) {
    if (infos == "") {
        return null;
    }

    let node = "";
    if (node_id != "0") {
        for(let i=0; i<infos.length; i++) {
            if (infos[i]['index'] == node_id) {
                node = {
                    index: infos[i]['index'],
                    form: infos[i]['form'],
                    pos: infos[i]['pos'],
                    head: infos[i]['head'],
                    label: infos[i]['label']
                };
                break;
            }
        }
    } else {
        node = {
            index: "0",
            form: "root",
            pos: "",
            head: "",
            label: ""
        };
    }
    
    let children = get_dependency_children(infos, node_id);
    if (children.length > 0) {
        node['children'] = children;
    }

    return node;
}

function get_dependency_children(infos, node_id) {
    let children = [];

    for (let i=0; i< infos.length; i++) {
        if(infos[i]['head'] == node_id) {
            children.push(build_dependency_node(infos, infos[i]['index']));
        }
    }

    return children;
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
.tree-container {
    margin: auto;
}
.graph-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.rich-media-node {
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  color: white;
  background-color: #e0cc15;
  border-radius: 4px;
}
</style>