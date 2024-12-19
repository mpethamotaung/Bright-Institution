document.addEventListener('DOMContentLoaded', function() {
    const roleRadios = document.querySelectorAll('input[name="role"]');
    const gradeField = document.getElementById('grade-field');
    const subjectsField = document.getElementById('subjects-field');

    roleRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.value === 'student') {
                gradeField.style.display = 'block';
                subjectsField.style.display = 'block';
            } else if (this.value === 'tutor') {
                gradeField.style.display = 'block';
                subjectsField.style.display = 'block';
            }
        });
    });

    // Initial visibility check
    if (document.querySelector('input[name="role"]:checked').value === 'student') {
        gradeField.style.display = 'block';
        subjectsField.style.display = 'block';
    } else {
        gradeField.style.display = 'block';
        subjectsField.style.display = 'block';
    }
});
