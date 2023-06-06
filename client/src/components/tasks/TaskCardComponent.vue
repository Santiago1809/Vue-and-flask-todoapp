<template>
  <div class="max-w-lg rounded overflow-hidden shadow-lg hover:bg-gray-300 cursor-pointer mx-6 my-2 relative">
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ nombreTarea }}</div>
      <small class="overflow-hidden text-xs">{{ descripcionTarea }}</small>
    </div>
    <div class="absolute right-4 bottom-4 flex">
      <div class="mr-2">
        <ModalComponent
          :text="'fa-solid fa-pen-to-square'"
          :tituloTarea="nombreTarea"
          :descripcionTarea="descripcionTarea"
          :id="id_grupo"
          :id_tarea="id_tarea"
          :EditarTarea="true"
          color="blue"
        />
      </div>
      <div>
        <ModalComponent
          :text="'fa-solid fa-trash'"
          :BorrarTarea="true"
          :id_tarea="id_tarea"
          :tituloTarea="nombreTarea" 
          :descripcionTarea="descripcionTarea"
          color="red"
        />
      </div>
    </div>
  </div>
</template>
<script>
import ModalComponent from "../ModalComponent.vue";
export default {
  name: "TaskCard",
  props: {
    id_tarea: Number,
    id_grupo: Number,
    nombreTarea: String,
    descripcionTarea: String,
  },
  components: {
    ModalComponent,
  },
};
</script>
