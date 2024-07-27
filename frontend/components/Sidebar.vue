<template>
    <div class="bg-white m-20 w-[292px] h-[368px] p-8 text-base font-poppins shadow-[0_0_8px_#d8d5d5]">
        <div class="w-[88%] flex items-center h-[36px] border-b border-[#e6e1e1]">
            <img class="mr-3" src="assets/dashboard.svg" alt="dashboard">
            Your Dashboard
        </div>
        <details class="my-5">
            <summary class="flex cursor-pointer justify-between mt-6">
                <div class="flex items-center">
                    <img class="mr-3" src="assets/box.svg" alt="box">
                    Products
                </div>
                <img src="assets/down.svg" alt="down" class="transition-transform ease-linear duration-400" id="down-arrow">
            </summary >
            <ul class="list-none">
                <li class="mt-5 ml-8 text-[#6C6C6C] cursor-pointer"><nuxt-link to="/manageProduct" exact-active-class="text-[#EA454C]">Product Management</nuxt-link></li>
                <li class="mt-5 ml-8 text-[#6C6C6C] cursor-pointer"><nuxt-link to="/addNewProduct" exact-active-class="text-[#EA454C]">Add New Product</nuxt-link></li>
            </ul>
        </details>
        <details class="my-5">
            <summary class="flex cursor-pointer justify-between mt-6">
                <div class="flex items-center">
                    <img class="mr-3" src="assets/calendar-check.svg" alt="box">
                    Events
                </div>
                <img src="assets/down.svg" alt="down" class="transition-transform ease-linear duration-400" id="down-arrow">
            </summary>
            <ul class="list-none">
                <li class="mt-5 ml-8 text-[#6C6C6C] cursor-pointer"><nuxt-link to="/manageEvent" exact-active-class="text-[#EA454C]">Events Management</nuxt-link></li>
                <li class="mt-5 ml-8 text-[#6C6C6C] cursor-pointer"><nuxt-link to="/addNewEvent" exact-active-class="text-[#EA454C]">Add New Event</nuxt-link></li>
            </ul>
        </details>
    </div>
</template>

<style scoped>
details[open] summary #down-arrow{
    transform: rotate(180deg);
}
</style>