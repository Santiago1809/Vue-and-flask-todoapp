<template>
  <div>
    <!-- Botón para abrir el modal -->
    <button
      @click="openModal"
      :class="`bg-${color}-500 hover:bg-${color}-700 text-white font-bold py-2 px-4 rounded mx-1`"
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
          <div class="bg-slate-200 px-4 py-5 sm:p-6">
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
    <div
      v-if="isModalOpen && BorrarGrupo"
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
            <h2 class="text-xl font-bold mb-4">Eliminar grupo</h2>
            <p>Está seguro de eliminar el grupo:</p>
            <form @submit="eliminarGrupo">
              <input
                type="text"
                :value="nombreGrupo"
                class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500"
                readonly
                @keydown.enter.prevent="eliminarGrupo"
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
                  class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-500 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm"
                >
                  Eliminar
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div
      v-if="isModalOpen && EditarTarea"
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
          <div class="bg-slate-200 px-4 py-5 sm:p-6">
            <!-- Contenido del modal -->
            <h2 class="text-xl font-bold mb-4">Actalizar tarea</h2>
            <form @submit.prevent="actualizarTarea">
              <input
                type="text"
                :value="tituloTarea"
                class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500"
                @input="tituloTarea = $event.target.value"
                @keydown.enter.prevent="actualizarTarea"
              />
              <input
                type="text"
                :value="descripcionTarea"
                class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500"
                @input="descripcionTarea = $event.target.value"
                @keydown.enter.prevent="actualizarTarea"
              />
              <h3>Cambiar de grupo:</h3>
              <select
                name="grupos"
                id="grupos"
                v-model="grupoNuevo"
                class="block appearance-none w-full bg-white border border-gray-300 text-gray-700 py-2 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              >
                <option
                  v-for="(grupo, index) in grupos"
                  :key="index"
                  :value="grupo.id_grupo"
                >
                  {{ grupo.nombre }}
                </option>
              </select>
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
    <div
      v-if="isModalOpen && BorrarTarea"
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
            <h2 class="text-xl font-bold mb-4">Eliminar tarea</h2>
            <p>Está seguro de eliminar la tarea:</p>
            <form @submit.prevent="eliminarTarea">
              <input
                type="text"
                :value="tituloTarea"
                class="w-full px-4 pointer-events-none py-2 rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500"
                @input="tituloTarea = $event.target.value"
                @keydown.enter.prevent="eliminarTarea"
              />
              <input
                type="text"
                :value="descripcionTarea"
                class="w-full px-4 py-2 pointer-events-none rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500"
                @input="descripcionTarea = $event.target.value"
                @keydown.enter.prevent="eliminarTarea"
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
                  class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-500 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm"
                >
                  Eliminar
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
      grupos: [],
      grupoNuevo: this.id,
    };
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
      this.getGroups();
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
          this.openModal = false;
          window.location.reload();
        });
    },
    eliminarGrupo() {
      fetch(`${base_url}/delete_group`, {
        method: "DELETE",
        body: JSON.stringify({
          id_grupo: this.id,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then(() => {
          this.openModal = false;
          window.location.reload();
        });
    },
    actualizarTarea() {
      fetch(`${base_url}/update_task`, {
        method: "POST",
        body: JSON.stringify({
          id_tarea: this.id_tarea,
          id_grupo: this.grupoNuevo,
          titulo: this.tituloTarea,
          descripcion: this.descripcionTarea,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then(() => {
          this.openModal = false;
          window.location.reload();
        });
    },
    getGroups() {
      fetch(`${base_url}/groups?id_usuario=${localStorage.getItem("usuario")}`)
        .then((response) => response.json())
        .then((data) => {
          data.map((grupo) =>
            this.grupos.push({ id_grupo: grupo.id_grupo, nombre: grupo.nombre })
          );
        });
    },
    eliminarTarea(){
      fetch(`${base_url}/delete_task?id_tarea=${this.id_tarea}`,{
        method: "DELETE"
      })
      .then((response) => response.json())
      .then(()=>{
        this.openModal = false
        window.location.reload()
      })
    }
  },
  props: {
    text: String,
    EditarGrupo: Boolean,
    BorrarGrupo: Boolean,
    nombreGrupo: String,
    tituloTarea: String,
    descripcionTarea: String,
    EditarTarea: Boolean,
    BorrarTarea: Boolean,
    id: Number,
    id_tarea: Number,
    color: {
      typeof: String,
      required: true,
    },
  },
};
</script>
