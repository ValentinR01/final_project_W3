<script>
  import ProjectCreationForm from '../../../components/organisms/Forms/ProjectCreationForm.svelte';

  export let data;
</script>

<div class='card card--wide block-center'>
  <ProjectCreationForm data={data}/>
</div>