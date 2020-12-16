<template>
  <div id="app">
    <div id="app">
      
      <div class="header">
        <h1>MIS FINANZAS</h1>
          <nav>
            <button v-on:click="init" v-if="is_auth" > Home </button>
            <button v-on:click="getBalance" v-if="is_auth" > Ingreso </button>
            <button v-on:click="getBalance" v-if="is_auth" > Egreso </button>
            <button v-if="is_auth" > Resumen </button>
            <button v-if="is_auth" > Consejo </button>
            <button v-if="is_auth" >Cerrar Sesión</button>
        </nav>
      </div>

      <div class="main-component">
          <img v-bind:src="require('./assets/logo.jpg')" alt="">
      </div>

      <div class="footer">
         <h2>Misión TIC 2022</h2>
      </div>
 
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',

  components: {
    
  },
  data: function(){

    return {
      is_auth: localStorage.getItem('isAuth') || false
          }
  },    
   methods: {
            },

}       

</script>

<style>

body{
margin: 0 0 0 0;
}
.header{
margin: 0%;
padding: 0;
width: 100%;
height: 5vh;
min-height: 50px;
background-color: #191970;
color:#ffffff ;
display: flex;
justify-content: space-between;
align-items: center;
}
.header h1{
width: 20%;
text-align: center;
}
.header nav {
height: 100%;
width: 39%;
display: flex;
justify-content: space-around;
align-items: center;
font-size: 20px;
}
.header nav button{
color: #fafdff;
background: #4e5283;
border: 1px solid #ffffff;
border-radius: 18px;
padding: 5px 10px;
}
.header nav button:hover{
color: #191970;
background: #feffff;
border: 1px solid #fdfdfd;
}
.footer h2{
background:#191970;
color:#f7f7fc ;
width: 100%;
height: 5%;
display: flex;
justify-content: center;
align-items: center;
position: fixed;
bottom:0;
}

</style>
