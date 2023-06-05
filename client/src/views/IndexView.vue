<template>
  <section class="h-screen">
    <div class="h-full flex">
      <!-- Left column container with background -->
      <div class="w-full lg:w-6/12 xl:w-6/12 bg-slate-600">
        <div class="h-full flex items-center justify-center">
          <h1 class="text-9xl text-white">Grupos</h1>
        </div>
      </div>

      <!-- Right column container -->
      <div class="w-full lg:w-6/12 xl:w-6/12 overflow-y-auto">
        <div v-for="(grupo, index) in grupos" :key="index">
          <router-link :to="`/tasks/${grupo.id}`">
            <Card :nombreGrupo="grupo.nombre" />
          </router-link>
        </div>
        <CardInput @grupo-agregado="agregarGrupo" />
      </div>
    </div>
  </section>
</template>
<script>
import Card from "../components/index/IndexCardComponent.vue";
import CardInput from "../components/index/IndexCardInputComponent.vue";

let base_url = "http://192.168.1.3:3000";
export default {
  name: "Index page",
  data() {
    return {
      grupos: [],
    };
  },
  mounted() {
    this.getGroups();
    document.title = "Grupos";
  },
  methods: {
    getGroups() {
      fetch(`${base_url}/groups?id_usuario=${localStorage.getItem("usuario")}`)
        .then((response) => response.json())
        .then((data) => {
          data.map((group) => {
            this.grupos.push({ nombre: group.nombre, id: group.id_grupo });
          });
        });

      this.$emit("grupos-cargados", this.grupos);
    },
    agregarGrupo(grupo) {
      this.grupos.push({ nombre: grupo, id: this.grupos.length + 1 });
    },
  },
  components: {
    Card,
    CardInput,
  },
};
</script>
