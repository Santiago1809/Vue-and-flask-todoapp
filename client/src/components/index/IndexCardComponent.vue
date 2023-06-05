<template>
  <div class="max-w-lg rounded overflow-hidden shadow-lg hover:bg-gray-300 cursor-pointer mx-6 my-2.5">
    <div class="px-6 py-4">
      <div class="font-bold text-xl mb-2">{{ nombreGrupo }}</div>
    </div>
  </div>
</template>
<script>
export default {
  name: "IndexCardComponent",
  props: {
    nombreGrupo: String
  }
};
</script>
