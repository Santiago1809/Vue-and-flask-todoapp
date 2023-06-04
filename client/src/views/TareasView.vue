<template>
  <div>
    <section class="h-screen">
    <div class="h-full flex">
      <!-- Left column container with background-->
      <div class="w-full lg:w-6/12 xl:w-6/12 bg-slate-600">
        <div class="h-full flex items-center justify-center">
          <h1 class="text-7xl text-white">{{ nombreGrupo }}</h1>
        </div>
      </div>

      <!-- Right column container -->
      <div class="w-full lg:w-6/12 xl:w-6/12">
        <div class="h-full flex flex-col justify-center">
          <div v-for="(tarea, index) in tareas" :key="index">
            <Card :nombreTarea="tarea.titulo" :descripcionTarea="tarea.descripcion"/>
          </div>
        </div>
      </div>
    </div>
  </section>
  </div>
</template>
<script>
import Card from "@/components/tasks/TaskCardComponent.vue"

let base_url = "http://localhost:3000"
export default {
  name: "TaskCard",
  data(){
    return {
      tareas: [],
      nombreGrupo: ""
    }
  },
  mounted(){
    this.getTasks(),
    this.getGroup()
  },
  components: {
    Card
  },
  methods: {
    getTasks(){
      fetch(`${base_url}/tasks?id_grupo=${parseInt(this.$route.params.id)}`)
      .then(response=>response.json())
      .then(data => {
        data.map((item)=>{
          this.tareas.push({titulo: item.titulo, descripcion: item.descripcion})
        })
      })
    },
    getGroup(){
      fetch(`${base_url}/group?id_grupo=${parseInt(this.$route.params.id)}`)
      .then(response=>response.json())
      .then(data=>{
        this.nombreGrupo = data.Grupo.nombre
      })
      
    }
  }
}
</script>