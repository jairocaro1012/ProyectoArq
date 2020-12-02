var app = new Vue({
    el: '#app',
    data: {
        datos: null,
    },
    methods: {
        f: function () {
            axios.get("http://ec2-35-175-130-185.compute-1.amazonaws.com:5000/prueba")
                .then(response => {
                    this.nombre = response.data.nombre;
                    this.datos2=response.data.datos2;
                    console.log(response.data)
                    console.log(this.nombe);
                    document.getElementById("prueba").innerHTML =this.nombre;
                    document.getElementById("prueba1").innerHTML =this.datos2;
                    
                })
                .catch(error => console.error(error));
        }
    }

})