<script>
import Alerta from "./AlertaComponent.vue";

let base_url = "http://localhost:3000";
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
          if (data.access == "allowed") {
            alert("Acceso permitido");
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
          if (data.register===1){
            alert("Registro completado")
          }else {
            this.alerta = true
          }
        });
    },
  },
  components: {
    Alerta,
  },
};
</script>
<template>
  <div>
    <div v-show="!registro">
      <Alerta
        msg="Usuario o contraseña incorrectos."
        titulo="Error al iniciar sesión: "
        v-show="alerta"
      />
      <div class="w-full max-w-md mx-auto mt-40 bg-gray-50">
        <div class="flex flex-col justify-between sm:flex-row">
          <div
            class="card w-full bg-slate-500 p-3 rounded h-full text-center sm:w-1/2 sm:p-0 items-center"
          >
            <div class="flex flex-col justify-center h-full">
              <h2 class="text-xl font-semibold text-white mt-10">
                No estás registrado?
              </h2>
              <p class="mt-10 mb-10 text-gray-300">
                Dale click al siguiente botón para registrarte:
              </p>
              <button
                class="mt-4 text-sm py-2 px-3 bg-blue-600 rounded hover:bg-blue-800 text-white font-bold"
                @click="registro = !registro"
              >
                Registrarme
              </button>
            </div>
          </div>
          <form
            @submit.prevent="loguinForm($event)"
            class="card w-full bg-blue-300 shadow-md rounded px-8 pt-6 pb-8 mb-8 max-w-500px sm:w-1/2 sm:ml-0"
          >
            <div>
              <h2 class="text-xl font-semibold mb-4">Inicio de sesión</h2>
              <input
                type="email"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                placeholder="Correo"
                v-model="correo"
              />
              <input
                type="password"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                placeholder="Contraseña"
                v-model="contraseña"
              />
              <button
                type="submit"
                class="w-full px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-700 mb-6"
              >
                Ingresar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div v-show="registro">
      <Alerta
        msg="Usuario ya existe"
        titulo="Error al intentar registrar: "
        v-show="alerta"
      />
      <div class="w-full max-w-md mx-auto mt-40 bg-gray-50">
        <div class="flex flex-col justify-between sm:flex-row">
          <div
            class="card w-full bg-slate-500 p-3 rounded h-full text-center sm:w-1/2 sm:p-0 items-center"
          >
            <div class="flex flex-col justify-center h-full">
              <h2 class="text-xl font-semibold text-white mt-10">
                Ya tienes cuenta?
              </h2>
              <p class="mt-10 mb-20 text-gray-300">
                Dale click al siguiente botón para ir a iniciar sesión:
              </p>
              <button
                class="mt-4 text-sm py-2 px-3 bg-blue-600 rounded hover:bg-blue-800 text-white font-bold"
                @click="registro = !registro"
              >
                Iniciar sesión
              </button>
            </div>
          </div>
          <form
            class="card w-full bg-blue-300 shadow-md rounded px-8 pt-6 pb-8 mb-8 max-w-500px sm:w-1/2 sm:ml-0"
            @submit.prevent="registerForm($event)"
          >
            <div>
              <h2 class="text-xl font-semibold mb-4">Registro</h2>
              <input
                type="email"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                placeholder="Correo"
                v-model="correo"
              />
              <input
                type="text"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                placeholder="Nombre"
                v-model="nombre"
              />
              <input
                type="password"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                placeholder="Contraseña"
                v-model="contraseña"
              />
              <button
                type="submit"
                class="w-full px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-700 mb-6"
              >
                Registrarme
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
