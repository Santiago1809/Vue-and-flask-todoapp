<script>
import Alerta from "./AlertaComponent.vue";
let base_url = "http://192.168.1.3:3000";
export default {
  name: "Login",
  data() {
    return {
      correo: "",
      contraseña: "",
      nombre: "",
      registro: false,
      alerta: false,
    };
  },
  watch: {
    registro(newRegistro) {
      this.getTitle();
    },
  },
  methods: {
    loguinForm() {
      fetch(`${base_url}/login`, {
        method: "POST",
        body: JSON.stringify({
          correo: this.correo,
          contraseña: this.contraseña,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data[0].access == "allowed") {
            localStorage.setItem("usuario", data[1].usuario.id_usuario);
            this.$router.push("/index");
          } else {
            this.alerta = true;
          }
        });
    },
    registerForm() {
      fetch(`${base_url}/register`, {
        method: "POST",
        body: JSON.stringify({
          nombre: this.nombre,
          correo: this.correo,
          contraseña: this.contraseña,
        }),
        headers: { "Content-Type": "application/json" },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data[0].register === 1) {
            localStorage.setItem("usuario", data[1].usuario.id_usuario);
            this.$router.push("/index");
          } else {
            this.alerta = true;
          }
        });
    },
    getTitle() {
      document.title = this.registro ? "Registro" : "Inicio de sesión";
    },
    lookSesionActive() {
      if (localStorage.getItem("usuario")) {
        this.$router.push("/index");
      }
    },
  },
  mounted() {
    this.getTitle();
    this.lookSesionActive();
  },
  components: {
    Alerta,
  },
};
</script>
<template>
  <section class="h-screen">
    <LogoutButton />
    <div class="h-full flex">
      <!-- Left column container with background -->
      <div class="w-full lg:w-6/12 xl:w-6/12 bg-slate-600">
        <div class="h-full flex-col flex items-center justify-center">
          <h1 class="text-9xl text-white">VueNotes</h1>
          <i class="fa-solid fa-note-sticky block text-white text-8xl"></i>
        </div>
      </div>

      <!-- Right column container -->
      <div class="w-full lg:w-6/12 xl:w-6/12 overflow-y-auto flex items-center justify-center">
        <div class="w-full max-w-md">
          <div class="bg-gray-300 shadow rounded px-8 pt-6 pb-8 mb-4">
            <h2 class="text-2xl font-semibold mb-6 text-center" v-show="!registro">Inicio de sesión</h2>
            <h2 class="text-2xl font-semibold mb-6 text-center" v-show="registro">Registro</h2>
            <form @submit.prevent="registro ? registerForm($event) : loguinForm($event)">
              <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="nombre" v-show="registro">
                  Nombre
                </label>
                <input
                  v-show="registro"
                  type="text"
                  id="nombre"
                  class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                  placeholder="Nombre"
                  v-model="nombre"
                />
              </div>
              <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                  Correo
                </label>
                <input
                  type="email"
                  id="email"
                  class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                  placeholder="Correo"
                  v-model="correo"
                />
              </div>
              <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                  Contraseña
                </label>
                <input
                  type="password"
                  id="password"
                  class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                  placeholder="Contraseña"
                  v-model="contraseña"
                />
              </div>
              <div class="flex items-center justify-center">
                <button
                  type="submit"
                  class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-700"
                >
                  {{ registro ? 'Registrarme' : 'Ingresar' }}
                </button>
              </div>
            </form>
          </div>
          <div class="text-center">
            <p class="text-gray-700">
              {{ registro ? 'Ya tienes cuenta?' : "No estás registrado?" }}
              <span
                class="text-blue-500 cursor-pointer"
                @click="registro = !registro"
              >
                {{ registro ? 'Inicia sesión aquí' : 'Regístrate aquí' }}
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
