<template>
  <section class="h-screen">
    <div class="h-full flex">
      <!-- Left column container with background-->
      <div class="w-full lg:w-6/12 xl:w-6/12 bg-slate-600">
        <div class="h-full flex items-center justify-center">
          <h1 class="text-9xl text-white">Grupos</h1>
        </div>
      </div>

      <!-- Right column container -->
      <div class="w-full lg:w-6/12 xl:w-6/12">
        <div class="h-full flex flex-col justify-center">
          <div v-for="(grupo, index) in grupos" :key="index">
            <Card :nombreGrupo="grupo.nombre" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Card from "../components/index/IndexCardComponent.vue";
let base_url = "http://localhost:3000";
export default {
  name: "Index page",
  data() {
    return {
      grupos: [],
    };
  },
  mounted() {
    this.getGroups();
    document.title = "Grupos"
  },
  methods: {
    getGroups() {
      fetch(`${base_url}/groups?id_usuario=${localStorage.getItem("usuario")}`)
        .then((response) => response.json())
        .then((data) => {
          data.map((group) => {
            this.grupos.push({'nombre':group.nombre, 'id':group.id_grupo});
          });
        });
    },
  },
  components: {
    Card,
  },
};
</script>
