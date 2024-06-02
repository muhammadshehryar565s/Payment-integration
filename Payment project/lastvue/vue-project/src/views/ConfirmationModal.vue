<template>
    <div v-if="visible" class="modal-overlay">
      <div class="modal-content">
        <h3>Confirm Payment</h3>
        <p>Are you sure you want to submit the payment?</p>
        <div class="button-group">
          <button @click="confirm" class="btn-confirm">Confirm</button>
          <button @click="cancel" class="btn-cancel">Cancel</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      visible: {
        type: Boolean,
        default: false,
      },
    },
    methods: {
      confirm() {
        this.$emit('confirm');
        alert("Payment Successful");
      },
      cancel() {
        this.$emit('cancel');
      },
    },
  };
  </script>
  
  <style>

  .btn-cancel {
    background-color: #f44336; 
    color: white;
  }
  .btn-confirm {
    background-color: #4CAF50; 
    color: white;
    margin-right: 4px;
  }
  .btn-confirm,
  .btn-cancel {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  .modal-overlay{
    background-color: rgb(200, 194, 194);
    border-radius: 5px;
    text-align: center;
    height: 200px;
    width: 500px;
    margin-top: 10%;
    margin-right: 25%;
    margin-left: 143px;
  }
  </style>
  