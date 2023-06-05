<template>
  <div
    class="max-w-lg rounded overflow-hidden shadow-lg hover:bg-gray-300 cursor-pointer mx-6 my-2.5"
  >
    <div class="px-6 py-4 flex justify-between items-center">
      <div class="font-bold text-xl mb-2">
        <router-link :to="ruta" class="hover:underline hover:text-blue-700">{{ nombreGrupo }}</router-link>
      </div>
      <div class="flex">
        <ModalComponent
          :text="'fa-solid fa-pen-to-square'"
          :nombreGrupo="nombreGrupo"
          :id="id"
          :EditarGrupo="true"
        />
        <ModalComponent :text="'fa-solid fa-trash'" />
      </div>
    </div>
  </div>
</template>

<script>
import ModalComponent from "../ModalComponent.vue";
export default {
  name: "IndexCardComponent",
  props: {
    nombreGrupo: String,
    ruta: String,
    id:Number
  },
  components: {
    ModalComponent,
  },
};
</script>
