<template>
    <div id="body">
        <div id="upper">
            <div id="circles">
                <span class="dot" id="black"></span>
                <span class="dot" id="blue"></span>
                <span class="dot" id="green"></span>
                <span class="dot" id="skin"></span>
            </div>

            <img :src="product.image" />



            <div id="rightpane">
                <div id="title">
                    <h1>{{ product.title }}</h1>
                    <img
                        src="https://static.vecteezy.com/system/resources/thumbnails/001/505/003/small/share-icon-free-vector.jpg">
                </div>
                <p id="TPC">TPC</p>
                <div id="rating">
                    <p>4.8<span>&starf;</span>| 15 Ratings</p>
                    <div class="line"></div>
                </div>

                <p id="price"><b></b> ${{ product.price }}</p>
                <p id="choose">Choose a Size</p>
                <div id="radio">
                    <p class="Size"><input type="radio" name="Size" class="size" value="Small" id="Small">Small</p>
                    <p class="Size"><input type="radio" name="Size" class="size" value="Medium" id="Medium">Medium</p>
                    <p class="Size"><input type="radio" name="Size" class="size" value="Large" id="Large">Large</p>
                    <p class="Size"><input type="radio" name="Size" class="size" value="Extra Large" id="Extra">Extra Large
                    </p>
                    <p class="Size"><input type="radio" name="Size" class="size" value="XXL" id="XXL">XXL</p>
                </div>
                <div class="line"></div>
                <div id="buttons">
                    <button id="cart"><img src="https://cdn-icons-png.flaticon.com/512/711/711895.png">
                        <p>Add To Cart</p>
                    </button>
                    <button id="buy"><img src="https://icon-library.com/images/current-icon/current-icon-1.jpg">
                        <p>Buy Now</p>
                    </button>
                </div>
            </div>
        </div>
        <div i="image_row">
            <img id="arrow1" class="arrow"
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuwFYGl859TlHkUrVFmrAvNWAOtPby6ZgWMg&usqp=CAU">
            <img class="images" :src="product.image">
            <img class="images" :src="product.image">
            <img class="images" :src="product.image">
            <img class="images" :src="product.image">
            <img id="arrow2" class="arrow"
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuwFYGl859TlHkUrVFmrAvNWAOtPby6ZgWMg&usqp=CAU">
        </div>
        <div id="Line"></div>
        <div>

            <p class="bottom"><b class="heading">Product Description</b><b class="text">{{ product.description }}</b> </p>
            <p class="bottom"><b class="heading">Product Details</b><b class="text"> {{ product.category }}</b></p>
        </div>

    </div>
</template>

<script>
export default {
    async asyncData({ params }) {
        const productId = params.id;

        const response = await fetch(`https://fakestoreapi.com/products/2`);
        const product = await response.json();
        console.log(product);
        return { product };
    },

}


</script>

<style scoped>
body {
    margin-left: 5%;
    margin-right: 5%;
    margin-top: 5%;
    margin-bottom: 30vh;
}

#upper {
    display: flex;
    flex-direction: row;
    margin-bottom: 5vh;
}

img {
    width: 38%;
    float: left;
    border-radius: 3vh;
    margin-right: 12%;
}

#rightpane {

    margin-top: 7%;
    display: flex;
    flex-direction: column;
}

#title {
    display: flex;
    flex-direction: row;
}

#title img {
    width: 3vb;
    height: 3vh;
    margin-right: 0%;
    margin-top: 2.3%;

}

#title h1 {
    font-size: 4.2vh;
    font-weight: 500;
    margin-right: 30%;
}

#TPC {
    font-size: 2.7vh;
    font-weight: 500;
    color: darkgray;
}

#rating {
    font-size: 1.7vh;
    font-weight: 500;
}

#rating span {
    font-size: 150%;
    color: rgb(48, 232, 41);
}

#price {
    margin-top: 5%;
    font-size: 7vh;
    font-weight: 500;
}

.line {
    width: 100%;
    background-color: gainsboro;
    height: .2%;
    margin-top: 1vh;
    margin-bottom: 1vh;
}

#choose {
    margin-top: 1.5vh;
    font-size: 2.5vh;
    color: darkgray;
    font-weight: 500;
    margin-bottom: 2%;
}

#radio {
    display: flex;
    flex-direction: row;
    margin-bottom: 5%;
}

.Size {

    margin-right: 5%;
    padding-top: .5vh;
    background-color: rgba(236, 239, 233, 0.974);
    padding-bottom: .5vh;
    border-radius: 1vh;
    padding-left: 1vh;
    padding-right: 1vh;
    color: gray;
    font-size: 1.8vh;
    display: flex;
    flex-direction: row;
}

.size {

    margin-right: 1vh;
    font-weight: 500;


}

.radio {
    padding-top: 10vh;
}

#cart img {
    width: 5vh;
    height: 3vh;
    border-radius: 0%;
    color: aquamarine;
    margin-right: -.05vh;
    padding-left: 2vh;
    -webkit-filter: invert(100%);
    filter: invert(100%);
}

#buy img {
    width: 5vh;
    height: 3vh;
    border-radius: 0%;
    color: aquamarine;
    margin-right: -1vh;
    padding-left: 2vh;
    -webkit-filter: invert(100%);
    filter: invert(100%);
}

#buttons {

    margin-top: 10%;
}

#cart {
    margin-left: 2vh;
    margin-right: 6vh;
    width: 39%;
    border-color: #f20e61;
    background-color: #f50c46;
    border-radius: 4vh;
    padding: 1.5vh;
    display: inline;
    padding-left: 5vh;
    padding-right: 5vh;
}

#cart p {

    font-size: 2vh;
    font-weight: 500;
    color: white;
    margin-left: 1vh;
}

#buy {
    margin-left: 2vh;
    margin-right: 6vh;
    width: 39%;
    border-color: black;
    background-color: #f50c46;
    border-radius: 4vh;
    padding: 1.5vh;
    display: inline;
    padding-left: 5vh;
    padding-right: 5vh;
}

#buy p {
    font-size: 2vh;
    font-weight: 500;
    color: white;
    margin-left: -2vh;
}

#Line {
    width: 100%;
    background-color: gainsboro;
    height: .5vh;
    margin-top: 35vh;
}

.bottom {
    margin-top: 3.5vh;

}

.heading {
    font-size: 3vh;
    font-weight: 700;
    display: flex;
    margin-bottom: 3vh;
}

.text {
    color: darkgray;
    font-weight: 500;
    font-size: 2vh;
}

#circles {
    display: flex;
    flex-direction: column;
    margin-top: 35vh;
    margin-right: 2vh;
}

.dot {
    height: 15px;
    width: 15px;
    background-color: black;
    border-radius: 50%;

    margin: 1.5vh;
}

#blue {
    background-color: aqua;
}

#green {
    background-color: aquamarine;
}

#skin {
    background-color: bisque;
}

#image_row {
    margin: 2vh;
    display: flex;
    flex-direction: row;
    width: 40%;
}

.arrow {
    width: 3vb;
    margin-right: 2vh;
    margin-top: 4vh;
}

.images {
    width: 13vh;
    height: 13vh;
    margin-bottom: 15vh;
    margin-right: 3.3vh;

}

#arrow1 {
    margin-left: 6.5vh;
}

#arrow2 {
    -webkit-transform: scaleX(-1);
    transform: scaleX(-1);
}

.Newsmall {
    background-color: aqua;
}</style>
