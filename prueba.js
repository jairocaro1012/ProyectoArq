var app = new Vue({
    el: '#app',
    data: {
        datos: null,
    },
    methods: {
        f: function () {
            axios.get("http://ec2-18-204-8-148.compute-1.amazonaws.com:5000/prueba")
                .then(response => {
                    this.nombre = response.data.nombre;
                    console.log(response.data)
                    console.log(this.nombe);
                    document.getElementById("prueba").innerHTML =this.nombre;
                })
                .catch(error => console.error(error));
        }
    }

})