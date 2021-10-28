<template>
<center>
  <a :href="`/insertar/`" class="btn btn-danger">Nuevo</a>
  <div class="col-sm-7"> 
  <div class="card text-white bg-dark mb-3" v-for="input in directory.edges" :key="input.id">
  <div class="card-header">
    <h1>{{ input.node.name }}</h1>
  </div>
  <div class="card-body">
    <h5 class="card-title">Descripcion</h5>
    <p class="card-text">{{ input.node.notes}}</p>
    <a :href="`/actualizar/${input.node.id}/${input.node.name}/${input.node.notes}`" class="btn btn-success">Editar</a>  
  </div>
</div>
</div>
  <br>
  
</center>
  
 
</template>
 
<script>
  import axios from 'axios'
  export default{
name: 'CompanyData',
    data(){
      return {
    directory: []
      }
    },
    async mounted () {
    try {
  var result = await axios({
    method: 'POST',
    url: 'http://localhost:8000/graphql',
    data: {
      query: `
      {
          allVideojuegos {
                    edges {
                    node {
                        id
                        name
                        notes
                    }
                    }
                }
      }
      `
    }
    })
    this.directory = result.data.data.allVideojuegos
    } catch (error) {
    console.error(error)
    }
    }
  }
</script>




