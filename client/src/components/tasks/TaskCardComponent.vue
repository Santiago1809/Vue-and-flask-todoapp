<template>
  <div
    class="max-w-lg rounded overflow-hidden shadow-lg hover:bg-gray-300 cursor-pointer mx-6 my-2"
  >
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ nombreTarea }}</div>
      <small>{{ descripcionTarea }}</small>
    </div>
  </div>
</template>
<script>
export default {
  name: "TaskCard",
  props: {
    nombreTarea: String,
    descripcionTarea: String
  }
}
</script>
