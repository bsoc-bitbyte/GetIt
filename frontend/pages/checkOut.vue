<template>
  <div
    v-if="loading"
    class="fixed z-50 backdrop-blur-[2px] h-[100vh] w-[100vw]"
  >
    <img
      src="../assets/loader.gif"
      class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50"
    />
  </div>
  <!--  -->
  <div
    class="main mt-[2rem] justify-start pr-[0rem] flex-col min-[1240px]:items-center min-[1240px]:pl-[7.69rem] max-[1239px]:px-[0.8rem]"
  >
    <div
      v-if="isCheckoutVisible"
      class="fixed inset-0 bg-white bg-opacity-75 backdrop-blur-sm z-40"
      @click="isCheckoutVisible = false"
    ></div>

    <!-- Checkout Component -->
    <transition name="modal">
      <checkoutComp
        v-if="isCheckoutVisible"
        class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-lg shadow-lg p-8 z-50"
        :ticket_price="price"
      />
    </transition>
    <div class="max-[1239px]:py-[0.5rem] min-[1240px]:py-[0rem] tracking-wider">
      <h2
        class="heading font-extrabold text-[3rem] min-[1240px]:ml-[2rem] tracking-wider pr-[0rem]"
      >
        Checkout
      </h2>
    </div>
    <div class="parent pr-[0rem]">
      <form class="pb-[2rem] pt-[0rem] max-[1239px]:pt-[3rem]" @submit.prevent>
        <div
          class="flex-items max-[1239px]:flex-col max-[1239px]:items-center min-[1240px]:flex min-[1240px]:justify-start min-[1240px]:mt-[2rem]"
        >
          <div
            class="main1 min-[1240px]:shadow-lg min-[1240px]:mr-[10rem] min-[1240px]:ml-[2rem]"
          >
            <div
              class="billing-address pt-[1rem] max-[1239px]:pb-[2.5rem] min-[1240px]:pb-[1rem] bg-white mx-[0.5rem] min-[1240px]:pl-[1rem] min-[1240px]:pr-[2rem]"
            >
              <div>
                <h2
                  class="TEXT2 text-[1.69rem] font-bold subpixel antialiased divide-gray-400/[.6]] py-[1rem] tracking-wider"
                >
                  Registration Details
                </h2>
                <hr />
              </div>
              <div class="form">
                <div class="name min-[1240px]:flex">
                  <div class="TEXT py-[0.5rem] px-[0.1rem]">
                    <label
                      for="firstName"
                      class="min-[1240px]:block subpixel-antialiased tracking-wider"
                      >FirstName</label
                    >
                    <input
                      type="text"
                      placeholder="First Name"
                      id="fn"
                      required
                      v-model.trim.lazy="formValue.firstName"
                      class="pl-[0.69rem] min-[1240px]:mr-[0.5rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                    />
                  </div>
                  <div class="TEXT py-[0.5rem] px-[0.1rem]">
                    <label
                      for="lastName"
                      class="min-[1240px]:block subpixel-antialiased tracking-wider"
                      >LastName</label
                    >
                    <input
                      type="text"
                      placeholder="Last Name"
                      id="ln"
                      required
                      v-model.trim.lazy="formValue.lastName"
                      class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                    />
                  </div>
                </div>

                <div class="name min-[1240px]:flex">
                  <div class="TEXT py-[0.5rem] px-[0.1rem]">
                    <label
                      for="email"
                      class="min-[1240px]:block subpixel-antialiased tracking-wider"
                      >Email Address</label
                    >
                    <input
                      type="email"
                      disabled
                      placeholder="Email"
                      id="email"
                      required
                      v-model.trim.lazy="formValue.email"
                      class="pl-[0.69rem] min-[1240px]:mr-[0.5rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                    />
                  </div>
                  <div class="TEXT py-[0.5rem] px-[0.1rem]">
                    <label
                      for="phone"
                      class="min-[1240px]:block subpixel-antialiased tracking-wider"
                      >Phone</label
                    >
                    <input
                      type="tel"
                      placeholder="Phone Number"
                      id="phone"
                      required
                      v-model.trim.number.lazy="formValue.phone"
                      class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                    />
                  </div>
                </div>

                <div class="remaining-credentials">
                  <div class="TEXT py-[0.7rem] px-[0.1rem]">
                    <label
                      for="hostel-address"
                      class="min-[1240px]:block subpixel-antialiased tracking-wider"
                      >Hostel Address</label
                    >
                    <textarea
                      id="address"
                      placeholder="Address"
                      required
                      v-model.trim.lazy="formValue.hostel_address"
                      class="border-2 border-gray-300 pl-[0.69rem] rounded-[0.4rem] w-full h-[4rem]"
                    />
                  </div>
                  <div class="min-[1240px]:flex">
                    <div class="TEXT py-[0.7rem] px-[0.1rem]">
                      <label
                        for="roll"
                        class="min-[1240px]:block subpixel-antialiased tracking-wider"
                        >Roll Number</label
                      >
                      <input
                        type="text"
                        placeholder="Roll"
                        id="roll"
                        required
                        v-model.trim.lazy="formValue.roll"
                        class="pl-[0.69rem] min-[1240px]:mr-[0.5rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                      />
                    </div>
                    <div class="TEXT py-[0.7rem] px-[0.1rem]">
                      <label
                        for="checked"
                        class="min-[1240px]:block subpixel-antialiased tracking-wider"
                        >Branch</label
                      >
                      <select
                        id="branch"
                        v-model.trim.lazy="formValue.branch"
                        required
                        class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                      >
                        <option value="" disabled>Select Branch</option>
                        <option value="Computer Science and Engineering">
                          CSE
                        </option>
                        <option
                          value="Electronics and Communications Engineering"
                        >
                          ECE
                        </option>
                        <option value="Mechanical Engineering">ME</option>
                        <option value="Smart Manufacturing">SM</option>
                        <option value="Design">Design</option>
                      </select>
                    </div>
                  </div>
                  <div class="w-full min-[1240px]:flex">
                    <div class="TEXT py-[0.7rem] px-[0.1rem]">
                      <label
                        for="checked"
                        class="min-[1240px]:block subpixel-antialiased tracking-wider"
                        >Gender</label
                      >
                      <select
                        id="gender"
                        v-model.trim.lazy="formValue.gender"
                        required
                        class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                      >
                        <option value="" disabled>Select Gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="prefer_not_to_say">
                          Prefer Not to Say
                        </option>
                      </select>
                    </div>
                    <div class="TEXT py-[0.7rem] px-[0.1rem]">
                      <label
                        for="checked"
                        class="min-[1240px]:block subpixel-antialiased tracking-wider"
                        >Batch</label
                      >
                      <select
                        id="batch"
                        v-model.trim.lazy="formValue.batch"
                        required
                        class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200"
                      >
                        <option value="" disabled>Select Batch</option>
                        <option value="2020">2020</option>
                        <option value="2021">2021</option>
                        <option value="2022">2022</option>
                        <option value="2023">2023</option>
                      </select>
                    </div>
                  </div>
                  <!-- <div class="check2 pt-[1rem]">
                    <input
                      type="checkbox"
                      id="check2"
                      v-model.trim.lazy="formValue.consent"
                      true-value="yes"
                      false-value="no"
                      class="box"
                    />
                    <label for="check2" class="check2 text-s tracking-wider"
                      >Save the data for future use</label
                    >
                  </div> -->
                </div>
              </div>
            </div>
          </div>
          <div
            class="right-panel min-[1240px]:ml-[3rem] max-[1239px]:pt-[0.25rem] min-[1240px]:pt-[1rem] min-[1240px]:pr-[2rem] lg:w-[30vw] w-[80vw] lg:m-0 m-auto"
          >
            <div
              class="review-panel flex flex-col justify-between min-[1240px]:shadow-lg min-[1240px]:px-[2rem] min-[1240px]:pb-[2rem] max-[1239px]:py-[1rem] min-[1240px]:mt-[2rem]"
            >
              <div class="flex-col">
                <div class="flex justify-between">
                  <h3 class="TEXT2 tracking-wider font-bold items-center">
                    Order Review
                  </h3>
                  <div class="dropdown-btn">
                    <button
                      class="drop-btn"
                      @click="toggleDropdowncart"
                      :class="{ 'rotate-180': isOpencart }"
                    >
                      <img
                        src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png"
                      />
                    </button>
                  </div>
                </div>
                <p class="text-slate-600 subpixel-antialiased tracking-wider">
                  {{ cartStore.cart.length }} items in cart
                </p>
              </div>
              <ul
                v-if="isOpencart"
                class=""
                v-for="item in cartStore.cart"
                :key="item.pid"
              >
                <li
                  class="flex flex-col space-y-3 py-6 text-left sm:flex-row sm:space-x-5 sm:space-y-0"
                >
                  <div class="shrink-0">
                    <img
                      class="h-24 w-24 max-w-full rounded-lg object-cover"
                      :src="item.cover_image"
                      alt=""
                    />
                  </div>
                  <div class="relative flex flex-1 flex-col justify-between">
                    <div class="sm:col-gap-5 sm:grid sm:grid-cols-2">
                      <div class="pr-8 sm:pr-5">
                        <p class="text-base font-semibold text-gray-700">
                          {{ item.title }}
                        </p>
                        <p class="mx-0 mt-1 mb-0 text-sm text-gray-400">
                          {{ item.location }}
                        </p>
                      </div>
                      <div
                        class="mt-4 flex items-end justify-between sm:mt-0 sm:items-start sm:justify-end"
                      >
                        <p
                          class="shrink-0 w-20 text-base font-semibold text-gray-700 sm:order-2 sm:ml-8 sm:text-right"
                        >
                          ₹{{ item.totalPrice }}
                        </p>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <div
              class="main3 min-[1240px]:shadow-lg pt-[2rem] mt-[1rem] pb-[1rem] min-[1240px]:px-[2rem] max-[1239px]:pt-[0rem]"
            >
              <div class="my-[2.5rem] divide-gray-400/[.4]">
                <div
                  class="billing-summary-dropdown flex justify-between flex-col"
                >
                  <div class="flex justify-between">
                    <h3
                      class="TEXT2 text-[1rem] font-bold subpixel antialiased tracking-wider"
                    >
                      Billing Summary
                    </h3>
                    <div class="dropdown-btn">
                      <button
                        class="drop-btn"
                        @click="toggleDropdown"
                        :class="{ 'rotate-180': isOpen }"
                      >
                        <img
                          src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png"
                          class="inline-block w-4 h-4 ml-1 transform transition"
                        />
                      </button>
                    </div>
                  </div>
                  <div v-if="isOpen" class="dropdown-content" style="">
                    <div class="px-2">
                      <div class="block p text-gray-600 w-full text-sm">
                        <option>Standard shipping - ₹0.00</option>
                      </div>
                      <div class="block p text-gray-600 w-full text-sm">
                        <option>
                          Total Product Price- ₹{{
                            cartStore.getPrice.toFixed(2)
                          }}
                        </option>
                      </div>
                    </div>
                  </div>
                </div>
                <hr />
                <div class="main1 flex justify-between">
                  <h3
                    class="TEXT2 text-[1rem] font-bold subpixel antialiased py-[1rem] tracking-wider"
                  >
                    Grand Total
                  </h3>
                  <h3 class="py-[1rem] tracking-wider">
                    ₹{{ cartStore.getPrice }}
                  </h3>
                </div>
                <div class="pt-[1rem] invisible">
                  <input
                    type="checkbox"
                    id="checked"
                    v-model.trim.lazy="formValue.checked"
                    true-value="yes"
                    false-value="no"
                    class="box"
                  />
                  <label
                    for="checked"
                    class="text-s text-slate-600 tracking-wider"
                    >Please check to acknowledge our Privacy & Terms
                    policy</label
                  >
                </div>
                <div class="submit-button pt-[1rem] flex justify-center">
                  <button
                    type="submit"
                    class="btn bg-#ea454c py-[1rem] min-[1240px]:px-[6rem] rounded-3xl max-[1239px]:w-full"
                    @click="submitForm"
                  >
                    Checkout
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script setup>
import { useCartStore } from "../store/index";
import { useAuthStore } from "../store/auth";
import { useRouter } from "vue-router";
import { reactive } from "vue";
import { toast } from "vue3-toastify";
import { useNuxtApp } from "#app";

const loading = ref(false);

const config = useRuntimeConfig();

const isOpen = ref(false);
const isOpencart = ref(false);

// Use your Pinia store
const cartStore = useCartStore();
const authStore = useAuthStore();
const router = useRouter();

const formValue = reactive({
  firstName: "",
  lastName: "",
  email: authStore.userEmail,
  hostel_address: "",
  roll: "",
  branch: "",
  gender: "",
  batch: "",
  phone: "",
  // consent: false,
  price: cartStore.getPrice,
  prod_name: "",
  prod_type: "ticket",
  prod_id: "2",
});
onMounted(async () => {
  const nuxtApp = useNuxtApp();
  try {
    console.log("hello");
    const response = await nuxtApp.$authenticatedFetch(
      `${config.public.API_BASE_URL}/api/accounts/me/`
    );

    console.log("respn", response);
    formValue.firstName = response.first_name;
    formValue.lastName = response.last_name;
    formValue.email = response.email;
    formValue.phone = response.phone_number;
    formValue.hostel_address = response.address;
  } catch (error) {
    // use the toast here
    toast.error("Error fetching User Data", {
      autoClose: 2000,
      position: toast.POSITION.BOTTOM_CENTER,
    });
    console.error("Error fetching User Data", error);
  }
});

const toggleDropdown = () => {
  isOpen.value = !isOpen.value;
};

const toggleDropdowncart = () => {
  isOpencart.value = !isOpencart.value;
};

const submitForm = async (e) => {
  if (
    !(
      formValue.firstName &&
      formValue.lastName &&
      formValue.email &&
      formValue.hostel_address &&
      formValue.roll &&
      formValue.branch &&
      formValue.gender &&
      formValue.batch &&
      formValue.phone
    )
  )
    return;
  e.preventDefault();
  const requestData = prepareRequestData();

  console.log(requestData);
  await createUPIGateway(requestData);
};

const createUPIGateway = async (requestData) => {
  try {
    // Your logic to make a request to the backend to get gateway
    loading.value = true;
    const response = await $fetch(
      `${config.public.API_BASE_URL}/api/tickets/create-upi-gateway/`,
      { method: "POST", body: { requestData } }
    );
    const redirect_url = response["data"]["payment_url"];
    loading.value = false;
    cartStore.clearCart();
    window.location.href = redirect_url;
  } catch (error) {
    console.error("Error:", error);
  }
};

const prepareOrderItems = () => {
  const orderItem = cartStore.cart.map((item) => ({
    id: item.id,
    title: item.title,
    price: item.ticket_price,
    quantity: item.quantity,
  }));
  return orderItem;
};

const prepareRequestData = () => {
  // Your logic to prepare request data
  console.log("formValue", formValue);
  return {
    first_name: formValue.firstName,
    last_name: formValue.lastName,
    email: authStore.userEmail,
    address: formValue.hostel_address,
    roll: formValue.roll,
    branch: formValue.branch,
    gender: formValue.gender,
    phone: formValue.phone,
    batch: formValue.batch,
    price: cartStore.getPrice,
    prod_name: cartStore.cart[0].title,
    order_items: prepareOrderItems(),
  };
};

const increase = () => {
  // Your logic to increase count
};

if (!authStore.isAuthenticated) {
  router.push("/Signin");
}
</script>

<style scoped>
.TEXT1 {
  font-family: poppins, sans-serif;
  font-weight: 700;
  font-smooth: always;
}

.TEXT {
  font-family: Open-Sans, sans-serif;
  color: rgb(101, 99, 99);
  font-smooth: always;
}

.TEXT2 {
  font-family: Inter, sans-serif;
  color: black;
  font-smooth: always;
}

.heading {
  font-family: poppins, sans-serif;
}

.btn {
  background-color: rgba(234, 69, 76, 1);
  color: #fff;
  font-family: Inter;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  font-smooth: always;
}

.comment {
  color: rgba(130, 130, 130, 1);
}

.main {
  position: static;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
}

.parent {
  overflow-x: hidden;
  right: 0;
  left: 0;
}

.box {
  accent-color: rgb(35, 162, 63);
}
.dropdown-title svg {
  transition: transform 0.3s;
}

.rotate-180 {
  transform: rotate(180deg);
}
.dropdown-title svg {
  transition: transform 0.3s;
}

.rotate-180 {
  transform: rotate(180deg);
}
</style>
