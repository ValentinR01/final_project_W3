<script>
  import Margin from "../../../components/atoms/Margin.svelte";
  import NewUserForm from "../../../components/organisms/Forms/NewUserForm.svelte";

  export let data;
</script>

<Margin marginTop='3%'>
  <div class='card card--wide block-center'>
    <NewUserForm data={data} />
  </div>
</Margin>