<template>
  <div>
    <!-- Botón para abrir el modal -->
    <button
      @click="openModal"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      <span><i :class="text"></i></span>
    </button>

    <!-- Modal -->
    <div
      v-if="isModalOpen && EditarGrupo"
      class="fixed z-10 inset-0 overflow-y-auto"
    >
      <div class="flex items-center justify-center min-h-screen px-4">
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
          aria-hidden="true"
        ></div>
        <div
          class="bg-white rounded-lg overflow-hidden shadow-xl transform transition-all sm:w-full sm:max-w-2xl"
        >
          <div class="bg-red-200 px-4 py-5 sm:p-6">
            <!-- Contenido del modal -->
            <h2 class="text-xl font-bold mb-4">Cambiar nombre de grupo</h2>
            <form @submit="actualizarGrupo">
              <input
                type="text"
                :value="nombreGrupo"
                class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500"
                @input="nombreGrupo = $event.target.value"
                @keydown.enter.prevent="actualizarGrupo()"
              />

              <div
                class="bg-gray-100 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse"
              >
                <!-- Botones para cerrar y guardar el modal -->
                <button
                  @click="closeModal"
                  class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-500 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm"
                >
                  Cerrar
                </button>
                <button
                  type="submit"
                  class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-500 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm"
                >
                  Guardar
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
let base_url = "http://192.168.1.3:3000";
export default {
  data() {
    return {
      isModalOpen: false,
    };
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    actualizarGrupo() {
      fetch(`${base_url}/edit_group`, {
        method: "PUT",
        body: JSON.stringify({
          id_grupo: this.id,
          nombre_grupo: this.nombreGrupo,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then(() => {
          this.openModal = false
          window.location.reload()
        });
    },
  },
  props: {
    text: String,
    EditarGrupo: Boolean,
    nombreGrupo: String,
    tarea: Boolean,
    id: Number,
  },
};
</script>
