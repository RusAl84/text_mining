<template>

  <v-container>
  <h1>Analisis</h1>

    <v-card>
      <v-card-title>
        Поиск синонимов
      </v-card-title>
      <v-card-text>
      <v-text-field v-model="word"
          label="синоним"
      ></v-text-field>
    <v-btn @click="onClick">
      Отправить
    </v-btn>
      </v-card-text>
    </v-card>
    <h1>{{response}}</h1>

</v-container>

</template>

<script>
import API from "@/api/api";
export default {
  name: "Analisis",
  // Модель данных страницы
  data: () => {
    return {
      word: '',
      response:'',
    }
  },
  methods: {
     onClick() {
      let resp=""
      try {
        resp =  API.get_sm(this.word)
        alert(resp)
        // router.push('/').catch(()=>{})
      } catch (e) {
        console.error(e)
      }
      this.response=resp
      // alert(store.state.authName)
    },
},

}
</script>

<style scoped>

</style>