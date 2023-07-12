<script>

  import RoomRegistrationForm from "../../../../components/organisms/Forms/RoomRegistrationForm.svelte";

  export let data;

</script>

<div class="card block-center">
  <RoomRegistrationForm data={data.booking}/>
</div>