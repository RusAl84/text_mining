<template>
  <!-- App.vue -->
  <v-app>
    <v-navigation-drawer app>
      <Drawner/>
    </v-navigation-drawer>

    <v-app-bar app>
      <!-- -->
      <router-link to="/">Home</router-link> |
      <router-link to="/analisis">Analisis</router-link> |
      <router-link to="/about">About</router-link>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>

        <!-- If using vue-router -->
        <router-view/>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>
<script>
// @ is an alias to /src
import Drawner from "@/components/Drawner";

export default {
  name: 'Home',
  components: {
    Drawner
  }
}
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
