<template>
 <center>
    <br>
    <div class="p-3 mb-2 bg-dark text-white">
        <h3 >ID: {{id=$route.params.id}} </h3><br>
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
    <button name="button" class="btn btn-primary" type="submit">Actualizar</button>
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
        name: this.$route.params.name,
        notes: this.$route.params.notes,
        id: '',
        directory: []
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
  updateVideojuego(input:{id:"`+this.id+`", name:"`+this.name+`",notes:"`+this.notes+`"}){
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
 
 
 
 

