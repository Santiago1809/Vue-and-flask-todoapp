<template>
  <div class="home">

    <LoginComponent />
  </div>
</template>

<script>

import LoginComponent from "@/components/LoginComponent.vue";

export default {
  name: "HomeView",
  components: {
    LoginComponent,
  },
};
</script>
