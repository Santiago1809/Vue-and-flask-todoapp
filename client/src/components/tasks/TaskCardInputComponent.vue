<template>
  <form
    class="max-w-lg rounded overflow-hidden shadow-lg mt-4 mx-6"
    @submit.prevent="add_task($event)"
  >
    <div class="flex items-center px-6 py-4 flex-col">
      <input
        type="text"
        class="flex-grow h-10 px-2 py-1 text-xl rounded-md focus:outline-none focus:border-blue-500"
        placeholder="Agrega el titulo de la tarea"
        v-model="titulo"
        required
      />
      <input
        type="text"
        class="flex-grow h-10 px-2 py-1 text-xl rounded-md focus:outline-none focus:border-blue-500"
        placeholder="Agrega la descripción"
        v-model="descripcion"
        required
      />
      <button type="submit">
        <span class="ml-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 4v16m8-8H4"
            />
          </svg>
        </span>
      </button>
    </div>
  </form>
</template>
<script>
let base_url = "http://192.168.1.3:3000";
export default {
  name: "TaskCardInput",
  data() {
    return {
      titulo: "",
      descripcion: "",
    };
  },
  methods: {
    add_task() {
      fetch(`${base_url}/create_task`, {
        method: "POST",
        body: JSON.stringify({
          titulo: this.titulo,
          descripcion: this.descripcion,
          id_grupo: this.$route.params.id,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then((data) => {
          this.$emit("tarea-agregado", data);
          this.titulo = "";
          this.descripcion = "";
        });
    },
  },
};
</script>
