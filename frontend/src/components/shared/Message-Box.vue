<template>
    <div v-if="msg !== ''"
        :class="msg === errorPhrase ? 'w-fit max-w-sm bg-gray-100 text-red-600 font-semibold rounded-lg shadow-md p-1 mx-auto mb-4' : 'w-fit max-w-sm bg-gray-100 text-gray-800 font-semibold rounded-lg shadow-md p-1 mx-auto mb-4'">
        <p>{{ msg }}</p>
    </div>
</template>

<script setup>
defineProps({
    msg: String,
    errorPhrase: String,
})
</script>