<script>
  import Margin from "../../../../components/atoms/Margin.svelte";
  import RoomRegistrationForm from "../../../../components/organisms/Forms/RoomRegistrationForm.svelte";

  export let data;

</script>

<Margin marginTop='10%'>
  <div class="card block-center">
    <RoomRegistrationForm data={data.booking}/>
  </div>
</Margin>