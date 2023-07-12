<script>
  import NewUserForm from "../../../components/organisms/Forms/NewUserForm.svelte";

  export let data;
</script>

<div class='card block-center'>
  <NewUserForm data={data} employeePicture={data.users[0].profile_pic}/>
</div>