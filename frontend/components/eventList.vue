<template>
    <div class="max-w-sm rounded-lg overflow-hidden shadow-lg hover:scale-[1.1] transition cursor-pointer ">
        <img class="w-full rounded-lg" :src="img_url" alt="Sunset in the mountains">
        <div class="px-4 pt-4 flex flex-row justify-between">
            <div class="font-bold text-2xl">{{ title }}</div>
            <span class="bg-[#ea454c] rounded-full px-3 py-1 text-sm font-semibold text-white">Rs. {{ ticket_price }}</span>
        </div>
        <div class="px-4 py-4 flex flex-row justify-between">
            <span class="bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">{{ location }}</span>
            <span class="bg-[#ea454c] rounded-full px-3 py-1 text-sm font-semibold text-white">{{ date }}</span>

        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true,
        },
        description: {
            type: String,
            required: true,
        },
        email: {
            type: String,
            required: true,
        },
        date: {
            type: String,
            required: true,
        },
        location: {
            type: String,
            required: true,
        },
        ticket_price: {
            type: String,
            required: true,
        },
        img_url: {
            type: String,
            required: true,
        }

    },
    name: 'eventList'
}
</script>
