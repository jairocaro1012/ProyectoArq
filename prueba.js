var app = new Vue({
    el: '#app',
    data: {
        datos: null,
        nombre: null,
        datos2:null
    },
    methods: {
        f: function () {
            axios.get("http://ec2-35-175-130-185.compute-1.amazonaws.com:5000/prueba")
                .then(response => {
                    this.nombre = response.data.nombre;
                    this.datos2=response.data.datos2;
                    this.datos3=response.data.datos3;
                    this.datos4=response.data.datos4;
                    this.datos5=response.data.datos5;
                    this.datos6=response.data.datos6;
                    this.datos7=response.data.datos7;
                    this.datos8=response.data.datos8;
                    this.datos9=response.data.datos9;
                    console.log(response.data)
                    console.log(this.nombre);
                    document.getElementById("prueba").innerHTML =this.nombre;
                    document.getElementById("prueba1").innerHTML =this.datos2;
                    document.getElementById("prueba2").innerHTML =this.datos3;
                    document.getElementById("prueba3").innerHTML =this.datos4;
                    document.getElementById("prueba4").innerHTML =this.datos5;
                    document.getElementById("prueba5").innerHTML =this.datos6;
                    document.getElementById("prueba6").innerHTML =this.datos7;
                    document.getElementById("prueba7").innerHTML =this.datos8;
                    document.getElementById("prueba8").innerHTML =this.datos9;
                    
                })
                .catch(error => console.error(error));
        }
    }

})