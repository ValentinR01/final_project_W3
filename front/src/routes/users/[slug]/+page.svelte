<script>
  import Margin from "../../../components/atoms/Margin.svelte";
  import UserForm from "../../../components/organisms/Forms/UserForm.svelte";

  export let data;
</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <UserForm data={data} />
  </div>
</Margin>