<template>
  <form
    class="max-w-lg rounded overflow-hidden shadow-lg mt-4"
    @submit.prevent="add_grupo()"
  >
    <div class="flex items-center px-6 py-4">
      <input
        type="text"
        class="flex-grow h-10 px-4 py-2 text-xl rounded-md focus:outline-none focus:border-blue-500"
        placeholder="Agrega un nuevo grupo"
        v-model="nuevo_grupo"
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
  name: "InputCardComponent",
  data() {
    return {
      nuevo_grupo: "",
    };
  },
  methods: {
    add_grupo() {
      fetch(`${base_url}/create_group`, {
        method: "POST",
        body: JSON.stringify({
          id_usuario: parseInt(localStorage.getItem("usuario")),
          nombre_grupo: this.nuevo_grupo,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then((data) => {
          this.$emit("grupo-agregado", data.Grupos.nombre);
          this.nuevo_grupo = "";
        });
    },
  },
};
</script>
