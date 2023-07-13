<template>
  <div class="max-lg:-mt-8">
    
    <div
      class="main  mt-[2rem] justify-start pr-[0rem] flex-col justify-center min-[1240px]:items-center min-[1240px]:pl-[7.69rem] max-[1239px]:px-[0.8rem]">
      <div class="max-[1239px]:py-[0.5rem] min-[1240px]:py-[0rem] tracking-wider">
        <h2
          class="heading font-extrabold max-lg:mt-16 text-[3rem] font-bold min-[1240px]:ml-[2rem] tracking-wider pr-[0rem]">
          Checkout</h2>
      </div>
      <div class="parent pr-[0rem]">
        <form @submit="submitForm" class="pb-[2rem] pt-[0rem] max-[1239px]:pt-[3rem]">
          <div
            class="flex-items max-[1239px]:flex-col max-[1239px]:items-center min-[1240px]:flex min-[1240px]:justify-start min-[1240px]:mt-[2rem]">
            <div class="main1 min-[1240px]:shadow-lg min-[1240px]:mr-[10rem] min-[1240px]:ml-[2rem]">
              <div
                class="billing-address pt-[1rem] max-[1239px]:pb-[2.5rem] min-[1240px]:pb-[1rem] bg-white mx-[0.5rem] min-[1240px]:pl-[1rem] min-[1240px]:pr-[2rem]">
                <div>
                  <h2
                    class="TEXT2 text-[1.69rem] font-bold subpixel antialiased  divide-gray-400/[.6]] py-[1rem] tracking-wider">
                    Billing Address</h2>
                  <hr>
                </div>
                <div class="form">
                  <div class="name min-[1240px]:flex">
                    <div class="TEXT py-[0.5rem] px-[0.1rem]">
                      <label for="firstName"
                        class="min-[1240px]:block subpixel-antialiased tracking-wider">FirstName</label>
                      <input type="text" placeholder="First Name" id="fn" v-model.trim.lazy="formValue.firstName"
                        class="pl-[0.69rem] min-[1240px]:mr-[0.5rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                    </div>
                    <div class="TEXT py-[0.5rem] px-[0.1rem]">
                      <label for="lastName"
                        class="min-[1240px]:block subpixel-antialiased tracking-wider">LastName</label>
                      <input type="text" placeholder="Last Name" id="ln" v-model.trim.lazy="formValue.lastName"
                        class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                    </div>
                  </div>
                  <div class="remaining-credentials">
                    <div class="TEXT py-[0.7rem] px-[0.1rem]">
                      <label for="email" class="min-[1240px]:block subpixel-antialiased tracking-wider">Email
                        Address</label>
                      <input type="email" placeholder="Email" id="email" v-model.trim.lazy="formValue.email"
                        class="pl-[0.69rem] w-full h-[2.5rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                    </div>
                    <div class="TEXT py-[0.7rem] px-[0.1rem]">
                      <label for="hostel-address" class="min-[1240px]:block subpixel-antialiased tracking-wider">Hostel
                        Address</label>
                      <textarea id="address" placeholder="Address" v-model.trim.lazy="formValue.hostel_address"
                        class="border-2 border-gray-300 pl-[0.69rem] rounded-[0.4rem] w-full h-[4rem]" />
                    </div>
                    <div class="min-[1240px]:flex">
                      <div class="TEXT py-[0.7rem] px-[0.1rem]">
                        <label for="roll" class="min-[1240px]:block subpixel-antialiased tracking-wider">Roll
                          Number</label>
                        <input type="text" placeholder="Roll" id="roll" v-model.trim.lazy="formValue.roll"
                          class="pl-[0.69rem]  min-[1240px]:mr-[0.5rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                      </div>
                      <div class="TEXT py-[0.7rem] px-[0.1rem]">
                        <label for="branch" class="min-[1240px]:block subpixel-antialiased tracking-wider">Branch</label>
                        <input type="text" placeholder="Branch" id="branch" v-model.trim.lazy="formValue.branch"
                          class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                      </div>
                    </div>
                    <div class="w-full min-[1240px]:flex">
                      <div class="TEXT py-[0.7rem] px-[0.1rem]">
                        <label for="checked" class="min-[1240px]:block subpixel-antialiased tracking-wider">Club
                          Member</label>
                        <input type="text" placeholder="Club Member" id="branch" v-model.trim.lazy="formValue.club_member"
                          class="pl-[0.69rem]  min-[1240px]:mr-[0.5rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                      </div>
                      <div class="TEXT py-[0.7rem] px-[0.1rem]">
                        <label for="phone" class="min-[1240px]:block subpixel-antialiased tracking-wider">Phone</label>
                        <input type="tel" placeholder="Phone Number" id="phone" v-model.trim.number.lazy="formValue.phone"
                          class="pl-[0.69rem] w-full h-[2.5rem] min-[1240px]:w-[17rem] rounded-[0.4rem] py-[0.25rem] border-2 border-gray-200">
                      </div>
                    </div>
                    <div class="check2 pt-[1rem]">
                      <input type="checkbox" id="check2" v-model.trim.lazy="formValue.consent" true-value="yes"
                        false-value="no" class="box">
                      <label for="check2" class="check2 text-s tracking-wider">Save the data for future use</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="right-panel min-[1240px]:ml-[3rem] max-[1239px]:pt-[0.25rem] min-[1240px]:pt-[1rem] min-[1240px]:pr-[2rem]">
              <div
                class="review-panel flex justify-between min-[1240px]:shadow-lg min-[1240px]:px-[2rem] min-[1240px]:pb-[2rem] max-[1239px]:py-[1rem] min-[1240px]:mt-[2rem]">
                <div class="flex-col">
                  <h3 class="TEXT2 tracking-wider font-bold items-center">
                    Order Review
                  </h3>
                  <p class="text-slate-600 subpixel-antialiased tracking-wider">
                    {{ count }} items in cart
                  </p>
                </div>
                <div class="dropdown-btn">
                  <button class="drop-btn">
                    <img src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png" />
                  </button>
                </div>
              </div>
              <div
                class="main3 min-[1240px]:shadow-lg pt-[2rem] mt-[1rem] pb-[1rem] min-[1240px]:px-[2rem] max-[1239px]:pt-[0rem]">
                <div class="my-[2.5rem] divide-gray-400/[.4]">
                  <div class="billing-summary-dropdown flex justify-between">
                    <div>
                      <h3 class="TEXT2 text-[1rem] font-bold subpixel antialiased tracking-wider">Billing Summary</h3>
                    </div>
                    <div class="dropdown-btn">
                      <button class="drop-btn">
                        <img src="https://img.icons8.com/ios-glyphs/30/000000/chevron-down.png" />
                      </button>
                    </div>
                  </div>
                  <hr>
                  <div class="main1 flex justify-between">
                    <h3 class="TEXT2 text-[1rem] font-bold subpixel antialiased py-[1rem] tracking-wider">Grand Total</h3>
                    <h3 class="py-[1rem] tracking-wider">Rs. {{ price }}</h3>
                  </div>
                  <div class="max-[1239px]:py-[0rem] min-[1240px]:py-[1rem]">
                    <div>
                      <label for="comment" class="comment tracking-wider heading text-gray-200">Order Comment
                      </label>
                    </div>
                    <div class="max-[1239px]:pb-[0.5rem] min-[1240px]:pb-[1.5rem]">
                      <textarea id="order-comment" placeholder="Type here..." v-model.trim.lazy="formValue.comment"
                        class="border-2 border-gray-300 pl-[0.69rem] rounded-[0.25rem] w-full h-[6rem]" />
                    </div>
                  </div>
                  <div class="pt-[1rem]">
                    <input type="checkbox" id="checked" v-model.trim.lazy="formValue.checked" true-value="yes"
                      false-value="no" class="box">
                    <label for="checked" class="text-s text-slate-600 tracking-wider">Please check to acknowledge our
                      Privacy & Terms policy</label>
                  </div>
                  <div class="submit-button pt-[1rem] flex  justify-center ">
                    <button type="submit" class="btn py-[1rem] min-[1240px]:px-[6rem] rounded-3xl max-[1239px]:w-full"
                      @click="submitForm">Checkout
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  layout: 'default',
  name: 'checkOut',
  data() {
    return {
      formValue: {
        firstName: '',
        lastName: '',
        email: '',
        hostel_address: '',
        roll: '',
        branch: '',
        club_member: '',
        phone: null,
        checked: '',
        comment: "",
        consent: 'no'
      },
      count: 0,
      price: 0
    }
  },
  methods: {
    submitForm(e) {
      e.preventDefault();
      console.log(this.formValue);
    },
    increase() {
      this.count++
    }
  },

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
  color: #FFF;
  font-family: Inter;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  font-smooth: always;
}

.comment {
  color: rgba(130, 130, 130, 1)
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
}</style>
