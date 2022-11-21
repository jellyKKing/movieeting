<template>
  <div>
    <div class="row">
      <div class="col">
        <div id="review-btn" data-bs-toggle="modal" data-bs-target="#exampleModal">
          <i class="bi bi-pencil-fill" style="font-size: 20px;"></i>
        </div>
      </div>
      <div class="col">
      </div>
    </div>
    <p>{{ movie_id }}</p>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content bg-body">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <input type="text" name="" id="">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieReview',
  props: {
    movie_id: String,
  },
}
</script>

<style lang="scss" scoped>
  #review-btn{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #212529;
    width: 3rem;
    height: 3rem;
    border: 1px solid hsla(210,16.7%,97.6%, 0.1);
    box-shadow: rgba(0, 0, 0, 0.2) 0px 20px 30px;    
    border-radius: 50%;
    transition: scale 0.3s;
    &:hover{
      cursor: pointer;
      scale: 103%;
    }
  }
</style>