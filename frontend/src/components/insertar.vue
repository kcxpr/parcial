<template>
 
  <center>
    <br>
    <div class="w3-container">
        <h2 style="background-color:powderblue;">Insertar un nuevo video juego</h2><br>
    <form action="" @submit.prevent="mounted()" >
  <div class="col-md-4">
    <label for="validationCustom01" class="form-label">Nombre del video juego</label>
    <input v-model="name" name="" type="text" class="form-control" id="validationCustom01" required>
    <div class="valid-feedback">
    </div>
  </div>
  <div class="col-md-4">
    <label for="validationCustom02" class="form-label">Descripcion</label>
    <input  v-model="notes" notes="" type="text" class="form-control" id="validationCustom02"  required>
    <div class="valid-feedback">
    </div>
  </div>
  <br>
  <div class="col-12">
    <button name="button" class="btn btn-primary" type="submit">Crear</button>
  </div>
</form>
</div>
  </center>
 
</template>
 
<script>
  import axios from 'axios'
  export default{
    name: 'CompanyData',
    data(){
      return {
        name: '',
        notes: '',
           directory: [],
      }
    },
    methods: {
    async mounted () {
  try {
        var result = await axios({
          method: 'POST',
          url: 'http://localhost:8000/graphql',
          data: {
            query: `
            mutation{
  createVideojuego(input:{name:"`+this.name+`",notes:"`+this.notes+`"}){
    videojuego{
      id
      name
      notes
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
}
</script>
