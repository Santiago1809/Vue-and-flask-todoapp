<template>
  <div>
    <logout-button-component />
    <section class="h-screen">
      <div class="h-full flex">
        <!-- Left column container with background -->
        <div class="w-full lg:w-6/12 xl:w-6/12 bg-slate-600">
          <div class="h-full flex items-center justify-center">
            <h1 class="text-7xl text-white">{{ nombreGrupo }}</h1>
          </div>
        </div>

        <!-- Right column container -->
        <div class="w-full lg:w-6/12 xl:w-6/12 overflow-y-auto bg-gray-100">
          <div class="h-full flex flex-col justify-center p-4">
            <div v-for="(tarea, index) in tareas" :key="index">
              <Card
                :id_grupo="tarea.id_grupo"
                :id_tarea="tarea.id_tarea"
                :nombreTarea="tarea.titulo"
                :descripcionTarea="tarea.descripcion"
              />
            </div>
            <CardInput @tarea-agregado="agregarTarea" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import Card from "@/components/tasks/TaskCardComponent.vue";
import CardInput from "@/components/tasks/TaskCardInputComponent.vue";
import LogoutButtonComponent from "../components/LogoutButtonComponent.vue";
let base_url = "http://192.168.1.3:3000";
export default {
  name: "TaskCard",
  data() {
    return {
      tareas: [],
      nombreGrupo: "",
    };
  },
  mounted() {
    this.getGroup(), this.getTasks();
    document.title = "Tareas";
  },
  components: {
    Card,
    CardInput,
    LogoutButtonComponent,
  },
  methods: {
    getTasks() {
      fetch(`${base_url}/tasks?id_grupo=${parseInt(this.$route.params.id)}`)
        .then((response) => response.json())
        .then((data) => {
          data.map((item) => {
            this.tareas.push({
              id_tarea: item.id_tarea,
              id_grupo: item.id_grupo,
              titulo: item.titulo,
              descripcion: item.descripcion,
            });
          });
        });
    },
    getGroup() {
      fetch(`${base_url}/group?id_grupo=${parseInt(this.$route.params.id)}`)
        .then((response) => response.json())
        .then((data) => {
          this.nombreGrupo = data.Grupo.nombre;
        });
    },
    agregarTarea(tarea) {
      this.tareas.push({
        id_grupo: tarea.id_grupo,
        id_tarea: tarea.id_tarea,
        titulo: tarea.titulo,
        descripcion: tarea.descripcion,
      });
    },
  },
};
</script>
