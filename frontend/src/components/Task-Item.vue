<template>
    <div class="w-full max-w-sm bg-gray-200 rounded-lg shadow-md p-6 mx-auto relative">
        <br>

        <!-- Task header -->
        <div class="flex items-center justify-between w-full">
            <h3 class="text-xl font-bold text-gray-800 mb-2">{{ task.title }}</h3>
            <h4 class="text-l font-semibold text-gray-800 mb-2">{{ task.mode }}</h4>
        </div>

        <!-- Task info -->
        <div class="flex text-xs mb-4">
            <div class="w-full">
                <label class="font-semibold">Deadline:</label>
                <br>
                <label>{{ task.deadlineDate }}
                    (<label>{{ task.remainingTime }}</label>)
                </label>
            </div>

            <div class="float-right self-center">
                <p class="font-semibold">{{ task.priority }}</p>
            </div>
        </div>

        <!-- Task description -->
        <div>
            <h4 class="font-semibold">Description:</h4>
            <div class="text-sm mb-4 overflow-x-auto h-40">
                <p class="overflow-y-hidden scrollbar-hide">{{ task.description }}</p>
            </div>
        </div>


        <!-- Utility-Buttons -->
        <div class="mb-2 absolute top-2 right-2">
            <button type="button"
                class="text-l w-fit bg-red-700 text-white px-2 rounded-md hover:bg-red-800 transition">Delete</button>
        </div>

        <div class="w-full flex justify-around">
            <button type="button"
                class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Edit</button>
            <button type="button"
                class="w-fit bg-green-600 text-white py-1 px-2 rounded-md hover:bg-green-800 transition">Done!</button>
        </div>
    </div>
</template>

<script setup>
defineProps({
    task: Object
})

</script>